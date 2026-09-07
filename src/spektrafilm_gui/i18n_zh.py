"""Simplified Chinese UI catalog.

Keys are the English strings exactly as they appear in the source; matching is
case- and whitespace-insensitive. Entries of the form ``context|key`` override
the plain entry for one parameter path, for example
``"film_render.halation|amount": "强度 (amount)"``.

Professional terms keep their English source in parentheses on first use, so
the wording stays checkable against the original documentation.
"""

from __future__ import annotations

ZH_UI: dict[str, str] = {
    # Tabs
    'MAIN': '主界面 (MAIN)',
    'FILM': '胶片 (FILM)',
    'PRINT': '相纸 (PRINT)',
    'ADVANCED': '高级 (ADVANCED)',
    'CONFIG': '配置 (CONFIG)',
    # Viewer footer
    'ccw rotate': '逆时针旋转 (ccw rotate)',
    'cw rotate': '顺时针旋转 (cw rotate)',
    'reset view': '重置视图 (reset view)',
    'Pixel of the screen mapped 1 to 1 to the image pixel': '屏幕像素与图像像素 1:1 映射',
    '2 screen pixels mapped to 1 image pixel': '2 个屏幕像素映射 1 个图像像素',
    '4 screen pixels mapped to 1 image pixel': '4 个屏幕像素映射 1 个图像像素',
    # Status bar
    'ready': '就绪 (ready)',
    # Actions
    'PREVIEW': '预览 (PREVIEW)',
    'SCAN': '扫描 (SCAN)',
    'SAVE': '保存 (SAVE)',
    # File pickers
    'Select input image': '选择输入图像',
    'No image selected': '未选择图像',
    'Select input raw': '选择输入 RAW 文件',
    'No raw selected': '未选择 RAW 文件',
    # Panels
    'napari layers': 'napari 图层',
}
