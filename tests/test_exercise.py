import pytest
import os

def test_exercise():
    os.chdir('src')

    import exercise

    input_values = ["ZSDRG204","Random","ZSDRG104","Test","ZSDRG304","Nothing",""]
    output = []

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)

    exercise.input = mock_input
    exercise.print = lambda s : output.append(s)

    exercise.main()

    assert output == ["Identifier? (empty will stop)","Name? (empty will stop)",\
                        "Identifier? (empty will stop)","Name? (empty will stop)",\
                            "Identifier? (empty will stop)","Name? (empty will stop)",\
                                "Identifier? (empty will stop)","==Items==","ZSDRG204: Random","ZSDRG104: Test","ZSDRG304: Nothing"]
