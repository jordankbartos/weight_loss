# widgets
from .widgets import (
    DateInput,
    FloatInput,
    InchesInput,
    IntInput,
    TimeInput,
    SelectionInput,
    BoolInput
)

items_list = [
    # name: (widget, value_type, default_value, column_title)
    {
        "widget_class": FloatInput,
        "widget_class_args": {},
        "type": float,
        "default_val": 0,
        "units": "lb",
        "col_title": "Weight",
    },
    {
        "widget_class": FloatInput,
        "widget_class_args": {},
        "type": float,
        "default_val": 0,
        "units": "%",
        'col_title': "Body Fat",
    },
    {
        "widget_class": FloatInput,
        "widget_class_args": {},
        "type": float,
        "default_val": 0,
        "units": None,
        'col_title': "BMI",
    },
    {
        "widget_class": FloatInput,
        "widget_class_args": {},
        "type": float,
        "default_val": 0,
        "units": "lb",
        'col_title': "Skeletal Muscle Mass",
    },
    {
        "widget_class": FloatInput,
        "widget_class_args": {},
        "type": float,
        "default_val": 0,
        "units": "lb",
        'col_title': "Bone Mass",
    },
    {
        "widget_class": FloatInput,
        "widget_class_args": {},
        "type": float,
        "default_val": 0,
        "units": "%",
        'col_title': "Body Water",
    },
    {
        "widget_class": InchesInput,
        "widget_class_args": {},
        "type": float,
        "default_val": 0,
        "units": "in",
        "col_title": "Waist",
    },
    {
        "widget_class": InchesInput,
        "widget_class_args": {},
        "type": float,
        "default_val": 0,
        "units": "in",
        "col_title": "Belly",
    },
    {
        "widget_class": InchesInput,
        "widget_class_args": {},
        "type": float,
        "default_val": 0,
        "units": "in",
        "col_title": "Hips",
    },
    {
        "widget_class": InchesInput,
        "widget_class_args": {},
        "type": float,
        "default_val": 0,
        "units": "in",
        "col_title": "Bicep",
    },
    {
        "widget_class": InchesInput,
        "widget_class_args": {},
        "type": float,
        "default_val": 0,
        "units": "in",
        "col_title": "Chest",
    },
    {
        "widget_class": InchesInput,
        "widget_class_args": {},
        "type": float,
        "default_val": 0,
        "units": "in",
        "col_title": "Thigh",
    },
    {
        "widget_class": InchesInput,
        "widget_class_args": {},
        "type": float,
        "default_val": 0,
        "units": "in",
        "col_title": "Calf",
    },
    {
        "widget_class": IntInput,
        "widget_class_args": {},
        "type": float,
        "default_val": 0,
        "units": "kcal",
        "col_title": "Target Calories",
    },
    {
        "widget_class": IntInput,
        "widget_class_args": {},
        "type": float,
        "default_val": 0,
        "units": "kcal",
        "col_title": "Consumed Calories",
    },
    {
        "widget_class": IntInput,
        "widget_class_args": {},
        "type": float,
        "default_val": 0,
        "units": "kcal",
        "col_title": "Active Calories",
    },

    {
        "widget_class": IntInput,
        "widget_class_args": {},
        "type": float,
        "default_val": 0,
        "units": "bpm",
        "col_title": "Resting Heart Rate",
    },
    {
        "widget_class": TimeInput,
        "widget_class_args": {},
        "type": float,
        "default_val": 0,
        "units": "min",
        "col_title": "Mile Time",
    },
    {
        "widget_class": BoolInput,
        "widget_class_args": {},
        "type": bool,
        "default_val": False,
        "units": None,
        "col_title": "Cardio",
    },
    {
        "widget_class": BoolInput,
        "widget_class_args": {},
        "type": bool,
        "default_val": False,
        "units": None,
        "col_title": "Workout",
    },
    {
        "widget_class": BoolInput,
        "widget_class_args": {},
        "type": bool,
        "default_val": False,
        "units": None,
        "col_title": "Meditate",
    },
    {
        "widget_class": BoolInput,
        "widget_class_args": {},
        "type": bool,
        "default_val": False,
        "units": None,
        "col_title": "Yoga",
    },
    {
        "widget_class": SelectionInput,
        "widget_class_args": {
            "options": ["Cutting", "Bulking", "Deload",]
        },
        "type": str,
        "default_val": "Cutting",
        "units": None,
        "col_title": "Mode",
    }
]
