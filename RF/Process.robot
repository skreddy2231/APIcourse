*** Settings ***
Documentation    resource file read
Resource        OM_Process.resource

*** Test Cases ***
1. Main tests
    PI Planning "Admin"
    Log     Done

