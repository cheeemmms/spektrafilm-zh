# spektrafilm 简体中文汉化分支

这是上游 [andreavolpato/spektrafilm](https://github.com/andreavolpato/spektrafilm)
（物理基的光谱胶片模拟软件）的**非官方简体中文汉化分支**。

> [!IMPORTANT]
> 本仓库仅对桌面 GUI 的**界面文案**做简体中文翻译，**不修改任何图像处理、
> 色彩科学或模拟逻辑**，因此渲染结果与上游完全一致。原项目版权归原作者
> Andrea Volpato 所有，汉化作者并未参与原项目开发。

## 这是什么软件

spektrafilm 从相机 RAW 或线性图像出发，基于胶片与相纸的**光谱数据**做逐像素
物理模拟，让你在虚拟负片 → 放大机 → 相纸 → 扫描的完整流程中交互式探索不同
胶片型号、成色剂、颗粒、光晕等效果对最终成像的影响。详见上游
[README](README.md)。

## 分支结构

| 分支 | 内容 |
|---|---|
| `main` | 与上游代码完全一致的镜像，始终可干净同步 |
| `zh-cn` | 简体中文汉化主线（本仓库默认分支），在 `main` 之上叠加翻译 |

## 中英文切换

- **默认显示中文**。
- 想恢复英文原界面：启动前设置环境变量
  `SPEKTRAFILM_LANG=en` 再运行即可，无需改动任何文件。

## 安装与运行

> [!NOTE]
> spektrafilm 与最新版 Python 不兼容，须使用 **Python 3.13**。

推荐用 `uv` 从本仓库安装并直接运行 GUI：

```bash
git clone https://github.com/cheeemmms/spektrafilm-zh.git
cd spektrafilm-zh

# 安装（含桌面 GUI 与 LUT 依赖）
uv pip install -e .

# 运行 GUI
spektrafilm
```

Windows 下也可直接双击仓库根目录的 `start.bat` 一键启动（无控制台窗口）。

## 汉化范围

- 窗口标题、标签页、底部工具条
- 各分区标题与全部参数名
- 所有参数的悬停说明（tooltip）
- 测光方式、白平衡、插值方式等下拉选项（仅显示译文，保存仍为英文原值）
- 状态栏与各类对话框的运行时提示

**刻意保留英文**（译名见词条表或悬停提示）：胶片/相纸型号、光源代号、
色彩空间与算法名（oklch、aces_rgc、cam16ucs、hanatos2025…）以及
Pro-Mist 等柔光镜商品名。专业术语一般在首次出现时括注英文原词，便于对照上游文档。

## 与上游同步

汉化在独立分支维护，可从上游拉取最新改动：

```bash
git fetch upstream
git checkout main && git merge upstream/main     # main 保持镜像
git checkout zh-cn && git merge main             # 将上游改动并入汉化主线
```

若上游修改了某个被翻译的文案，覆盖率测试
（`tests/test_i18n.py` 的 `test_controller_status_templates_are_translated` 等）
会报红提示缺少词条，避免翻译静默失效。

## 许可

沿用上游 `GPLv3`；JSON 配置与 LUT 遵循上游各自的 CC BY-SA 4.0 与自定义许可。
请完整保留上游的 [LICENSE](LICENSE)、[CITATION.cff](CITATION.cff) 与
[SPEKTRAFILM_LICENSE.txt](SPEKTRAFILM_LICENSE.txt)。
