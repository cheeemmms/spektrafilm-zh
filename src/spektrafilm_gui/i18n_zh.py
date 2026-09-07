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
    'input': '输入 (input)',
    'output': '输出 (output)',
    'crop and upscale': '裁剪与放大 (crop and upscale)',
    'exposure control': '曝光控制 (exposure control)',
    'profiles': '模拟配置 (profiles)',
    'enlarger': '放大机 (enlarger)',
    'tune': '微调 (tune)',
    'experimental': '实验性 (experimental)',
    'gui parameters': '界面参数 (gui parameters)',
    'display': '显示 (display)',
    'import raw': '导入 RAW (import raw)',
    'import rgb': '导入 RGB (import rgb)',
    # Parameter groups
    'Couplers': 'DIR 成色剂 (couplers)',
    'Halation': '光晕 (halation)',
    'Grain': '颗粒 (grain)',
    'Glare': '相纸反光 (glare)',
    'Chemistry': '显影化学 (chemistry)',
    'Preflash': '预闪 (preflash)',
    'Camera': '相机 (camera)',
    'Diffusion': '柔光镜 (diffusion)',
    'Scanner': '扫描仪 (scanner)',
    'Input gamut compress': '输入色域压缩 (input gamut compress)',
    'Output gamut compress': '输出色域压缩 (output gamut compress)',
    # DIR couplers
    'active': '启用 (active)',
    'amount': '强度 (amount)',
    'inhibition samelayer': '同层抑制 (inhibition samelayer)',
    'inhibition interlayer': '层间抑制 (inhibition interlayer)',
    'gamma samelayer rgb': '同层 gamma RGB (gamma samelayer rgb)',
    'gamma interlayer r to gb': '层间 gamma R→GB (gamma interlayer r to gb)',
    'gamma interlayer g to rb': '层间 gamma G→RB (gamma interlayer g to rb)',
    'gamma interlayer b to rg': '层间 gamma B→RG (gamma interlayer b to rg)',
    'diffusion size um': '扩散尺寸 μm (diffusion size um)',
    # Halation
    'scatter amount': '散射强度 (scatter amount)',
    'scatter spatial scale': '散射空间尺度 (scatter spatial scale)',
    'halation amount': '光晕强度 (halation amount)',
    'halation spatial scale': '光晕空间尺度 (halation spatial scale)',
    'boost ev': '高光提升 EV (boost ev)',
    'protect ev': '保护量 EV (protect ev)',
    'boost range': '提升过渡 (boost range)',
    'scatter core um': '散射核心 μm (scatter core um)',
    'scatter tail um': '散射拖尾 μm (scatter tail um)',
    'scatter tail weight': '散射拖尾权重 (scatter tail weight)',
    'halation strength': '光晕幅度 (halation strength)',
    'halation first sigma um': '首次反射 sigma μm (halation first sigma um)',
    'halation n bounces': '反射次数 (halation n bounces)',
    'halation bounce decay': '反射衰减 (halation bounce decay)',
    'halation renormalize': '光晕归一化 (halation renormalize)',
    # Grain
    'sublayers active': '启用子层结构 (sublayers active)',
    'particle area um2': '颗粒面积 μm² (particle area um2)',
    'particle scale': '颗粒尺度 RGB (particle scale)',
    'particle scale layers': '颗粒尺度·子层 (particle scale layers)',
    'density min': '最小密度 (density min)',
    'uniformity': '均匀度 (uniformity)',
    'blur': '模糊 (blur)',
    'blur dye clouds um': '染料云模糊 μm (blur dye clouds um)',
    'micro structure': '微观结构 (micro structure)',
    # Glare
    'percent': '比例 (percent)',
    'roughness': '粗糙度 (roughness)',
    # Chemistry
    'gamma factor': 'gamma 系数 (gamma factor)',
    'gamma factor fast': 'gamma 系数·快层 (gamma factor fast)',
    'gamma factor slow': 'gamma 系数·慢层 (gamma factor slow)',
    'gamma factor red': 'gamma 系数·红 (gamma factor red)',
    'gamma factor green': 'gamma 系数·绿 (gamma factor green)',
    'gamma factor blue': 'gamma 系数·蓝 (gamma factor blue)',
    'developer exhaustion': '显影液疲竭 (developer exhaustion)',
    # Preflash
    'exposure': '曝光 (exposure)',
    'y filter shift': '黄滤色片偏移 (y filter shift)',
    'm filter shift': '品红滤色片偏移 (m filter shift)',
    # Camera
    'film format mm': '画幅长边 mm (film format mm)',
    'lens blur um': '镜头模糊 μm (lens blur um)',
    'auto exposure method': '测光方式 (auto exposure method)',
    'auto exposure': '自动曝光 (auto exposure)',
    'exposure compensation ev': '曝光补偿 EV (exposure compensation ev)',
    # Diffusion filter
    'filter family': '滤镜系列 (filter family)',
    'strength': '滤镜档位 (strength)',
    'spatial scale': '空间尺度 (spatial scale)',
    'halo warmth': '光环暖度 (halo warmth)',
    'core intensity': '核心强度 (core intensity)',
    'core size': '核心尺寸 (core size)',
    'halo intensity': '光环强度 (halo intensity)',
    'halo size': '光环尺寸 (halo size)',
    'bloom intensity': '泛光强度 (bloom intensity)',
    'bloom size': '泛光尺寸 (bloom size)',
    # Scanner
    'lens blur': '镜头模糊 (lens blur)',
    'white correction': '白点校正 (white correction)',
    'white level': '白点电平 (white level)',
    'black correction': '黑点校正 (black correction)',
    'black level': '黑点电平 (black level)',
    'unsharp mask': 'USM 锐化 (unsharp mask)',
    # Gamut compress
    'algorithm': '算法 (algorithm)',
    'knee': '拐点 (knee)',
    # Input image
    'input color space': '输入色彩空间 (input color space)',
    'apply cctf decoding': '应用 CCTF 解码 (apply cctf decoding)',
    'upscale factor': '放大倍率 (upscale factor)',
    'crop': '裁剪 (crop)',
    'crop center': '裁剪中心 (crop center)',
    'crop size': '裁剪尺寸 (crop size)',
    'spectral upsampling': '光谱升采样 (spectral upsampling)',
    'hanatos2025 adaptation window': 'hanatos2025 适应窗口 (hanatos2025 adaptation window)',
    'hanatos2025 adaptation surface': 'hanatos2025 适应曲面 (hanatos2025 adaptation surface)',
    'spectral gaussian blur': '光谱高斯模糊 (spectral gaussian blur)',
    # Special and tune
    'film channel swap': '底片通道交换 (film channel swap)',
    'print channel swap': '相纸通道交换 (print channel swap)',
    'film gamma factor': '底片 gamma 系数 (film gamma factor)',
    # Display
    'use display transform': '使用显示变换 (use display transform)',
    'gray 18% canvas': '18% 灰背景 (gray 18% canvas)',
    'white padding': '白边留白 (white padding)',
    'preview max size': '预览最大尺寸 (preview max size)',
    'output interpolation': '输出插值 (output interpolation)',
    # Simulation
    'film profile': '胶片型号 (film profile)',
    'print profile': '相纸型号 (print profile)',
    'print illuminant': '放大光源 (print illuminant)',
    'print auto compensation': '自动补偿放大曝光 (print auto compensation)',
    'print exposure': '放大曝光 (print exposure)',
    'print y filter shift': '放大黄滤色片偏移 (print y filter shift)',
    'print m filter shift': '放大品红滤色片偏移 (print m filter shift)',
    'output color space': '输出色彩空间 (output color space)',
    'saving color space': '保存色彩空间 (saving color space)',
    'saving cctf encoding': '保存 CCTF 编码 (saving cctf encoding)',
    'auto preview': '自动预览 (auto preview)',
    'scan film': '扫描底片 (scan film)',
    'scan for print': '扫描（放大模式）(scan for print)',
    # Load raw
    'white balance': '白平衡 (white balance)',
    'temperature': '色温 (temperature)',
    'tint': '色调 (tint)',
    'lens correction': '镜头校正 (lens correction)',
    # GUI config actions
    'save current as default': '存为默认 (save current as default)',
    'save current to file': '保存到文件 (save current to file)',
    'load from file': '从文件加载 (load from file)',
    'restore factory default': '恢复出厂默认 (restore factory default)',
    'select file': '选择文件 (select file)',
    'reprocess raw': '重新处理 RAW (reprocess raw)',
    'update': '更新 (update)',
}
