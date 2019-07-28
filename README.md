# App
Personal App Design

This Repo contains Apps Designed by Malachi Liberda with the python module Kivy.

The file exampleApp.py is for testing purposes and as an example app currently, for reference when programming other Apps.

---exampleApp.py---
Explanation of File System:

All filed - exampleApp.py && my.kv

my.kv Explanation -
my.kv is for the styling of the app. The reason it is named my.kv is related to the class in the main file(exampleApp.py). The main class is exampleApp.py is MyApp. Therefore, we remove the "App" aspect of that string and we name the .kv file the preceding string in all lowercase.

Alternate Example: Class is named HelloApp, we name the .kv file hello.kv
Second Example: Class is named BruceSpringsteen, we name the .kv file brucespringsteen.kv since we have no "App" string to remove, we just lowercase the entire string.

To clarify, when main class is run, it looks for a file called "classname.kv". So in our case, when we run exampleApp.py, and it calls class MyApp, kivy looks for a file called my.kv and runs it.
