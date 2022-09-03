import datetime
import numpy as np

# import ipywidgets as widgets
from ipywidgets import (
    IntText,
    FloatText,
    Checkbox,
    Layout,
    DatePicker,
    Dropdown,
    HBox,
    HTML,
)

class DataEntryWidget:
    def __init__(self, label, units, layout=None):
        self.units=units
        if self.units is not None:
            self.lbl_text = f"{label} ({self.units})"
        else:
            self.lbl_text = label

        self.label = HTML(f"<b>{self.lbl_text}:</b>", layout=Layout(width="100px"))

        if layout is None:
            self.layout = Layout(width="max-content")
        else:
            self.layout = layout

    def to_box(self):
        raise NotImplementedError("must implement to_box")

    def get_col_title(self):
        return self.lbl_text

class IntInput(DataEntryWidget):
    def __init__(self, label, units, value=0, disabled=False, layout=None):
        super(IntInput, self).__init__(label=label, units=units, layout=layout)

        self.input = IntText(
            value=value,
            disabled=disabled
        )
        self.value = value
        self.disabled = disabled

    def to_box(self):
        return HBox([self.label, self.input], layout=self.layout)

    @property
    def value(self):
        return self.input.value

    @value.setter
    def value(self, value):
        if not (value is None or np.isnan(value)):
            self.input.value = value
        else:
            self.input.value = 0

class FloatInput(DataEntryWidget):
    def __init__(self, label, units, value=0, disabled=False, layout=None):
        super(FloatInput, self).__init__(label=label, units=units, layout=layout)

        self.input = FloatText(
            value=value,
            disabled=disabled
        )
        self.value = value
        self.disabled = disabled

    @property
    def value(self):
        return self.input.value

    @value.setter
    def value(self, value):
        
        self.input.value = value

    def to_box(self):
        return HBox([self.label, self.input])

class TimeInput(DataEntryWidget):
    def __init__(self, label, units, value=0, disabled=False, layout=None):
        super(TimeInput, self).__init__(label=label, units=units, layout=layout)
        self.minutes_input = IntText(
            disabled=disabled
        )

        self.seconds_input = IntText(
            disabled=disabled
        )
        self.value = value
        self.disabled = disabled

    @property
    def disabled(self):
        return self._disabled

    @disabled.setter
    def disabled(self, value):
        self.minutes_input.disabled = value
        self.seconds_input.disabled = value
        self._disabled = value

    @property
    def value(self):
        return self.minutes_input.value + (self.seconds_input.value / 60)

    @value.setter
    def value(self, value):
        if isinstance(value, float) and not np.isnan(value):
            self.minutes_input.value = int(value)
            self.seconds_input.value = int((value - int(value)) * 60)
        else:
            self.minutes_input.value = 0
            self.seconds_input.value = 0

    def to_box(self):
        return HBox([self.label, self.minutes_input, HTML("m"), self.seconds_input, HTML("s")], layout=self.layout)


class InchesInput(DataEntryWidget):
    def __init__(self, label, units, disabled=False, layout=None, value=None):
        super(InchesInput, self).__init__(label=label, units=units, layout=layout)
        self.inches_input = IntText(
            step=1,
            disabled=disabled
        )

        self.numerator_input = IntText(
            step=1,
            disabled=disabled
        )

        self.denominator_input = Dropdown(
            options=[2, 4, 8, 16, 32, 64],
            disabled=disabled
        )
        self.value = value
        self.disabled = disabled

    def to_box(self):
        return HBox([self.label, self.inches_input, HTML("and"), self.numerator_input, HTML("/"), self.denominator_input])

    @property
    def value(self):
        return self.inches_input.value + (self.numerator_input.value / self.denominator_input.value)

    @value.setter
    def value(self, value):
        if value is not None and not np.isnan(value):
            value = float(value).as_integer_ratio()
            inches = value[0] // value[1]
            numerator = value[0] % value[1]
            denominator = value[1]
        else:
            inches = 0
            numerator = 0
            denominator = 8

        self.inches_input.value = inches
        self.numerator_input.value = numerator
        self.denominator_input.value = denominator if denominator != 1 else 8

    @property
    def disabled(self):
        return self.disabled

    @disabled.setter
    def disabled(self, value):
        self._disabled = value
        self.inches_input.disabled = value
        self.numerator_input.disabled = value
        self.denominator_input.disabled = value

class DateInput(DataEntryWidget):
    def __init__(self, label, units, disabled=False, layout=None, value=None):
        super(DateInput, self).__init__(label=label, units=units, layout=layout)

        self.date_input = DatePicker(
            value=value,
            disabled=disabled
        )
        if value is None:
            self.value = datetime.date.today()
        else:
            self.value = value

        self.disabled = disabled

    def to_box(self):
        return HBox([self.label, self.date_input])

    @property
    def value(self):
        return self.date_input.value

    @value.setter
    def value(self, value):
        self.date_input.value = value

    @property
    def disabled(self):
        return self.date_input.disabled

    @disabled.setter
    def disabled(self, value):
        self.date_input.disabled = value

    def observe(self, func, names):
        self.date_input.observe(func, names=names)

class BoolInput(DataEntryWidget):
    def __init__(self, label, units, disabled=False, layout=None, value=None):
        super(BoolInput, self).__init__(label=label, units=units, layout=layout)
        self.input = Checkbox(disabled=disabled, indent=False)
        self.disabled = disabled
        self.value = value  

    @property
    def disabled(self):
        return self.input.disabled

    @disabled.setter
    def disabled(self, value):
        self.input.disabled = value

    @property
    def value(self):
        return self.input.value

    @value.setter
    def value(self, value):
        if isinstance(value, bool):
            self.input.value = value
        else:
            self.input.value = False

    def to_box(self):
        return HBox([self.label, self.input])

class SelectionInput(DataEntryWidget):
    def __init__(self, label, units, options, disabled=False, layout=None, value=None):
        super(SelectionInput, self).__init__(label=label, units=units, layout=layout)

        self.input = Dropdown(options=options)

    @property
    def disabled(self):
        return self.input.disabled

    @disabled.setter
    def disabled(self, value):
        self.input.disabled = value

    @property
    def value(self):
        return self.input.value

    @value.setter
    def value(self, value):
        self.input.value = value

    def to_box(self):
        return HBox([self.label, self.input])
