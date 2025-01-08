import comfy.ui as ui
import comfy.nodes as nodes

class VideoResolutionNode(nodes.Node):
    @classmethod
    def NODE_NAME(cls):
        return "Video Resolutions"

    @classmethod
    def CATEGORY(cls):
        return "Utility"

    @classmethod
    def INPUTS(cls):
        return []

    @classmethod
    def OUTPUTS(cls):
        return {
            "width": int,
            "height": int
        }

    def __init__(self):
        super().__init__()
        self.resolutions = {
            "Select a resolution": (0, 0),
            "=2.39:1 Cinescope/Theatrical=": (0, 0),
            "384x160": (384, 160),
            "480x200": (480, 200),
            "528x224": (528, 224),
            "624x256": (624, 256),
            "768x320": (768, 320),
            "864x352": (864, 352),
            "960x400": (960, 400),
            "1152x480": (1152, 480),
            "1248x512": (1248, 512),
            "1344x560": (1344, 560),
            "1440x576": (1440, 576),

            "=16x9=": (0, 0),
            "256x144": (256, 144),
            "512x288": (512, 288),
            "768x432": (768, 432),
            "1024x576": (1024, 576),
            "1280x720": (1280, 720),

            "=4x3=": (0, 0),
            "320x240": (320, 240),
            "336x252": (336, 252),
            "352x264": (352, 264),
            "368x276": (368, 276),
            "384x288": (384, 288),
            "400x300": (400, 300),
            "416x312": (416, 312),
            "432x324": (432, 324),
            "448x336": (448, 336),
            "464x348": (464, 348),
            "496x372": (496, 372),
            "512x384": (512, 384),
            "528x396": (528, 396),
            "544x408": (544, 408),
            "560x420": (560, 420),
            "576x432": (576, 432),
            "592x444": (592, 444),
            "608x456": (608, 456),
            "624x468": (624, 468),
            "640x480": (640, 480),
            "656x492": (656, 492),
            "672x504": (672, 504),
            "688x516": (688, 516),
            "704x528": (704, 528),
            "736x552": (736, 552),
            "752x564": (752, 564),
            "768x576": (768, 576),
            "784x588": (784, 588),
            "800x600": (800, 600),
            "816x612": (816, 612),
            "832x624": (832, 624),
            "864x648": (864, 648),
            "896x672": (896, 672),
            "912x684": (912, 684),
            "928x696": (928, 696),
            "944x708": (944, 708),
            "960x720": (960, 720),
            "976x732": (976, 732),
            "992x744": (992, 744),
            "1008x756": (1008, 756),
            "1024x768": (1024, 768),
            "1072x804": (1072, 804),
            "1088x816": (1088, 816),
            "1120x840": (1120, 840),
            "1152x864": (1152, 864),
            "1168x876": (1168, 876),
            "1184x888": (1184, 888),
            "1200x900": (1200, 900),
            "1264x948": (1264, 948),
            "1280x960": (1280, 960)
        }
        self.selected_resolution = list(self.resolutions.keys())[0]
        self.horizontal_alignment = False
        self.add_input_ports()
        self.add_output_ports()

    def add_input_ports(self):
        pass

    def add_output_ports(self):
        for output_name, output_type in self.OUTPUTS().items():
            self.add_output_port(output_name, output_type)

    def process(self):
        width, height = self.resolutions[self.selected_resolution]
        return {
            "width": width,
            "height": height
        }

    def build_ui(self):
        def on_resolution_change(new_resolution):
            self.selected_resolution = new_resolution

        self.add_widget(
            ui.Dropdown(
                items=list(self.resolutions.keys()),
                default=self.selected_resolution,
                callback=on_resolution_change,
                label="Select Resolution"
            )
        )

        def on_alignment_toggle(new_value):
            if isinstance(new_value, str):
                new_value = (new_value.lower() == "true")
            self.horizontal_alignment = new_value
            self.update_output_alignment()

        self.add_widget(
            ui.Toggle(
                default=self.horizontal_alignment,
                callback=on_alignment_toggle,
                label="Horizontal Alignment"
            )
        )

    def update_output_alignment(self):
        if self.horizontal_alignment:
            self.set_output_alignment("horizontal")
        else:
            self.set_output_alignment("vertical")

    def set_output_alignment(self, alignment):
        if alignment == "horizontal":
            self.set_output_port_layout({
                "width":  {"row": 0, "column": 0},
                "height": {"row": 0, "column": 1},
            })
        elif alignment == "vertical":
            self.set_output_port_layout({
                "width":  {"row": 0, "column": 0},
                "height": {"row": 1, "column": 0},
            })

nodes.register_node(VideoResolutionNode)

NODE_CLASS_MAPPINGS = {
    "Text Overlay": VideoResolutionNode,
}
