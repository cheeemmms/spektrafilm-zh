"""Translation layer behaviour and catalog coverage.

The coverage test is what keeps translations from silently rotting: every shell
string the GUI hardcodes must exist in the Chinese catalog, so a rename
upstream fails here instead of quietly falling back to English at runtime.
"""

from __future__ import annotations

import unittest

from spektrafilm_gui import i18n
from spektrafilm_gui.i18n_zh import ZH_UI


SHELL_TEXTS = (
    'MAIN',
    'FILM',
    'PRINT',
    'ADVANCED',
    'CONFIG',
    'ccw rotate',
    'cw rotate',
    'reset view',
    'ready',
    'PREVIEW',
    'SCAN',
    'SAVE',
    'Select input image',
    'No image selected',
    'Select input raw',
    'No raw selected',
    'napari layers',
    'Pixel of the screen mapped 1 to 1 to the image pixel',
    '2 screen pixels mapped to 1 image pixel',
    '4 screen pixels mapped to 1 image pixel',
)


def _key(text: str) -> str:
    return ' '.join(text.split()).casefold()


def _manifest_labels() -> tuple[str, ...]:
    """Every label the manifests can put on screen, titles included."""
    from spektrafilm_gui import param_manifest as pm

    specs = [
        *pm.INPUT_IMAGE_FIELDS,
        *pm.SPECIAL_FIELDS,
        *pm.DISPLAY_PANEL_FIELDS,
        *pm.SIMULATION_FIELDS,
    ]
    for manifest in pm.ALL_MANIFESTS:
        specs.extend(manifest.fields)

    labels = [manifest.title for manifest in pm.ALL_MANIFESTS]
    labels.extend(spec.label or spec.leaf.replace('_', ' ') for spec in specs)
    return tuple(labels)


class TranslationTests(unittest.TestCase):
    def setUp(self) -> None:
        i18n.set_language('zh')
        i18n.reset_missing_entries()

    def tearDown(self) -> None:
        i18n.set_language('zh')

    def test_shell_texts_are_translated(self) -> None:
        keys = {_key(key) for key in ZH_UI}
        self.assertEqual([text for text in SHELL_TEXTS if _key(text) not in keys], [])

    def test_manifest_labels_are_translated(self) -> None:
        keys = {_key(key) for key in ZH_UI}
        self.assertEqual([text for text in _manifest_labels() if _key(text) not in keys], [])

    def test_translated_label_is_returned_untouched(self) -> None:
        self.assertEqual(i18n.tr('MAIN'), ZH_UI['MAIN'])

    def test_unknown_label_falls_back_to_lowercase(self) -> None:
        self.assertEqual(i18n.tr('Some Unknown Label'), 'some unknown label')

    def test_unknown_sentence_keeps_capitalisation(self) -> None:
        self.assertEqual(i18n.tr_verbatim('Some Unknown Sentence'), 'Some Unknown Sentence')

    def test_missing_entries_are_reported(self) -> None:
        i18n.tr('Some Unknown Label')
        self.assertIn('some unknown label', i18n.missing_entries())

    def test_english_mode_is_untranslated(self) -> None:
        i18n.set_language('en')
        self.assertEqual(i18n.tr('MAIN'), 'main')
        self.assertEqual(i18n.tr_verbatim('MAIN'), 'MAIN')


if __name__ == '__main__':
    unittest.main()
