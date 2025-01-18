import nodes
import torch
import comfy.model_management

class HunyuanResolutions:
    @classmethod
    def INPUT_TYPES(s):
        aspect_ratios = [
            "256x256 (1:1)",
            "256x384 (2:3)",
            "384x256 (3:2)",
            "320x448 (5:7)",
            "448x320 (7:5)",
            "384x512 (3:4)",
            "512x384 (4:3)",
            "512x512 (1:1)",
            "512x768 (2:3)",
            "768x512 (3:2)",
            "512x640 (4:5)",
            "640x512 (5:4)",
            "448x768 (9:16)",
            "768x448 (16:9)",
            "576x1024 (9:16)",
            "704x1408 (1:2)",
            "704x1344 (13:25)",
            "768x1344 (4:7)",
            "768x1280 (3:5)",
            "832x1216 (2:3)",
            "832x1152 (5:7)",
            "896x1152 (7:9)",
            "896x1088 (4:5)",
            "960x1088 (8:9)",
            "960x1024 (15:16)",
            "1024x1024 (1:1)",
            "1024x960 (16:15)",
            "1088x960 (9:8)",
            "1088x896 (5:4)",
            "1152x896 (9:7)",
            "1152x832 (7:5)",
            "1216x832 (3:2)",
            "1280x768 (5:3)",
            "1344x768 (7:4)",
            "1344x704 (16:9)",
            "1024x576 (16:9)",
            "1408x704 (2:1)",
            "1472x704 (21:10)",
            "1536x640 (12:5)",
            "1600x640 (5:2)",
            "1664x576 (3:1)",
            "1728x576 (3:1)"
        ]

        return {"required": {
            "resolution": (aspect_ratios, ),
        }}

    RETURN_NAMES = ("Width", "Height")
    RETURN_TYPES = ("INT", "INT")
    FUNCTION = "generate"
    CATEGORY = "Utilities"

    def generate(self, resolution):
        # Parse resolution string to get dimensions
        dimensions = resolution.split(' ')[0]
        width, height = map(int, dimensions.split('x'))

        # Ensure dimensions are multiples of 16
        width = int((width // 16) * 16)
        height = int((height // 16) * 16)

        return (width, height)

NODE_CLASS_MAPPINGS = {
    "HunyuanResolutions": HunyuanResolutions,
}
