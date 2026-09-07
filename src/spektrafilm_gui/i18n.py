"""UI text translation entry points.

Two entry points, because the untranslated UI treats the two kinds of text
differently:

``tr``
    Short labels (parameter names, panel titles, buttons). Falls back to the
    lowercased source text, which is how the English UI renders them.
``tr_verbatim``
    Sentences (tooltips, status messages). Falls back to the source text
    untouched, since capitalisation carries meaning there.

A catalog maps the original English text to its translation. Keys are matched
case- and whitespace-insensitively, so reformatting the source string does not
silently drop a translation. An optional ``context`` scopes an entry to one
parameter path when the same word needs different translations in different
panels.

With no active catalog every call returns the original behaviour, so the
English UI is bit-for-bit unchanged.
"""

from __future__ import annotations

import os
from importlib import import_module

ENV_LANGUAGE = 'SPEKTRAFILM_LANG'
CONTEXT_SEPARATOR = '|'
DEFAULT_LANGUAGE = 'zh'

_CATALOG_MODULES = {'zh': 'spektrafilm_gui.i18n_zh'}

_language = DEFAULT_LANGUAGE
_catalog: dict[str, str] | None = None
_missing: set[str] = set()


def _normalize_language(value: str | None) -> str:
    if value is None:
        return DEFAULT_LANGUAGE
    normalized = value.strip().lower()
    return normalized or DEFAULT_LANGUAGE


def _normalize_key(text: str) -> str:
    return ' '.join(text.split()).casefold()


def _load_catalog() -> dict[str, str]:
    global _catalog
    if _catalog is None:
        module_name = _CATALOG_MODULES.get(_language)
        if module_name is None:
            _catalog = {}
        else:
            entries = getattr(import_module(module_name), 'ZH_UI')
            _catalog = {_normalize_key(key): value for key, value in entries.items()}
    return _catalog


def _lookup(text: str, context: str | None, report: bool) -> str | None:
    catalog = _load_catalog()
    if not catalog:
        return None

    key = _normalize_key(text)
    if context:
        scoped = catalog.get(_normalize_key(context) + CONTEXT_SEPARATOR + key)
        if scoped is not None:
            return scoped

    translated = catalog.get(key)
    if translated is None and report:
        _missing.add(key)
    return translated


def set_language(language: str) -> None:
    global _language, _catalog
    _language = _normalize_language(language)
    _catalog = None


def current_language() -> str:
    return _language


def tr(text: str, *, context: str | None = None, report: bool = True) -> str:
    """Translate a short label.

    ``report`` is off for values that are intentionally left in English, such
    as product or algorithm names in a dropdown, so they do not pollute the
    missing-entry report.
    """
    translated = _lookup(text, context, report)
    return translated if translated is not None else text.lower()


def tr_verbatim(text: str, *, context: str | None = None, report: bool = True) -> str:
    translated = _lookup(text, context, report)
    return translated if translated is not None else text


def missing_entries() -> tuple[str, ...]:
    return tuple(sorted(_missing))


def reset_missing_entries() -> None:
    _missing.clear()


def write_missing_report(path: str) -> int:
    entries = missing_entries()
    with open(path, 'w', encoding='utf-8') as report:
        for entry in entries:
            report.write(entry + '\n')
    return len(entries)


set_language(os.environ.get(ENV_LANGUAGE))
