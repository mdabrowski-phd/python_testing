*** Settings ***
Library     SeleniumLibrary
Library     ScreenCapLibrary

Test Setup    Start Video Recording
Test Teardown    Stop Video Recording
Suite Teardown    Close All Browsers

*** Variables ***
${BROWSER}  headlesschrome
${NOTHEADLESS}=    "headlesschrome" not in "${BROWSER}" or True

*** Test Cases ***
Search On Google
    Open Browser   http://www.google.com   ${BROWSER}
    Run Keyword If    ${NOTHEADLESS}   Wait Until Page Contains Element   L2AGLb
    Run Keyword If    ${NOTHEADLESS}   Click Element   css=button[id="L2AGLb"]
    Unselect Frame
    Input Text     name=q   Stephen\ Hawking
    Press Keys     name=q   SPACE
    Press Keys     name=q   ENTER
    Wait Until Page Contains Element   id=res
    Page Should Contain   Wikipedia
    Close Window
