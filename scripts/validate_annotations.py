import json
from pathlib import Path

DATASET_FILE = Path("dataset/annotations.json")


def validate_annotations():
    if not DATASET_FILE.exists():
        print("ERROR: annotations.json not found.")
        return

    with open(DATASET_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    errors = []

    if not isinstance(data, list):
        errors.append("Dataset must be a JSON list.")

    for index, item in enumerate(data, start=1):
        required_fields = [
            "image_id",
            "image_type",
            "objects",
            "visual_attributes",
            "qa",
            "annotation_status",
        ]

        for field in required_fields:
            if field not in item:
                errors.append(
                    f"Item {index}: missing required field '{field}'."
                )

        if "objects" in item:
            for obj in item["objects"]:
                if "label" not in obj:
                    errors.append(f"Item {index}: object missing label.")
                if "count" not in obj:
                    errors.append(f"Item {index}: object missing count.")
                if "confidence" not in obj:
                    errors.append(
                        f"Item {index}: object missing confidence."
                    )

        if "qa" in item:
            qa_fields = [
                "question",
                "answer",
                "evidence",
                "confidence",
            ]

            for field in qa_fields:
                if field not in item["qa"]:
                    errors.append(
                        f"Item {index}: QA missing '{field}'."
                    )

    if errors:
        print("VALIDATION FAILED")
        for error in errors:
            print("-", error)
    else:
        print("VALIDATION PASSED")
        print(f"Validated {len(data)} annotation records.")


if __name__ == "__main__":
    validate_annotations()
