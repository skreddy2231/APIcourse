*** Settings ***
Documentation    Below documentation helps to understand highlevel Test Approach and
...         sprint based agile process
#python -m robot.libdoc <library or path to resource file> <output name>.html


*** Keywords ***
PI Planning "${user}"
    [Documentation]    ** PLENAIR ** Productiehuis PI planning Q4-2023
    ...     Goal:
    ...     | Goal is load stories in backlog |
    ...     | Plan stories in sprint Iterations |

    ...     Under PI Planning:
    ...     - Sprint(8.0.62) Plan and estimate story point(s)
    ...     - Stories refinement
    ...     - Stories Delivery
    [Tags]    PI
    log    Goal is load stories in backlog for next 4 sprints
    [Arguments]    scrum_master
    FOR    ${user}    IN    {1,2,3,4}
        Log     Done
    END
