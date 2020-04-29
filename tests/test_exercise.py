import pytest
import src.exercise

def test_exercise():
    input_values = ["ZSDRG204","Random","ZSDRG104","Test","ZSDRG304","Nothing",""]
    input_values_stored = ["1","2"]
    output = []

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    assert output == ["Identifier? (empty will stop)","Name? (empty will stop)",\
                        "Identifier? (empty will stop)","Name? (empty will stop)",\
                            "Identifier? (empty will stop)","Name? (empty will stop)",\
                                "","==Items==","ZSDRG204: Random","ZSDRG104: Test","ZSDRG304: Nothing"]
