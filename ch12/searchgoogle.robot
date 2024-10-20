*** Settings ***
Library     SeleniumLibrary
Library     ScreenCapLibrary

Test Setup    Start Video Recording
Test Teardown    Stop Video Recording
Suite Teardown    Close All Browsers

*** Test Cases ***
Search On Google
    Open Browser   http://www.google.com   Chrome
    Wait Until Page Contains Element   L2AGLb
    Click Element   css=button[id="L2AGLb"]
    Input Text     name=q   Stephen\ Hawking
    Press Keys     name=q   ENTER
    Page Should Contain   Wikipedia
    Close Window
