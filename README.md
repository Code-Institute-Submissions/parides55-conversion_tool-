# ***CONVERSION TOOL***

Conversion Tool is a Python terminal program, which runs in the Code Institute mock terminal on Heroku.

This program offers the opportunity to the user to make currency and unit conversions by using the Frankfurter API and the SymPy librrary. The Frankfurter API tracks the foreign exchange references rates published by the European Central Bank and the data refreshes around 16:00 CET every working day. The SymPy library offers the unit conversions based on the SI system and also many other scientific equations and calculations which are not part of this project.

Click here to use the program

![Responsive mockup](assets/README_screenshots/responsive_mockup_opti.jpg)

<details>

<summary><b>Table of Content</b>(click to open)</summary>

- [***CONVERSION TOOL***](#conversion-tool)
  - [How to use it](#how-to-use-it)
  - [Features](#features)
      - [Existing Features](#existing-features)
      - [Future Features](#future-features)
  - [Data Model](#data-model)
  - [Testing](#testing)
  - [Bugs](#bugs)
  - [Validator Testing](#validator-testing)
  - [Deployment](#deployment)
  - [Credits](#credits)

</details>

## How to use it


When the program first runs, it provides the user with some selections, where the user can choose what to convert, Currency or Units.
![StartUp screen](assets/README_screenshots/start_up_screen_opti.jpg)

If Currency Conversion is selected, immediately a list of all available currency codes is shown to clearly indicate to the user what codes can be selected.
![Currency screen](assets/README_screenshots/currency_screen_opti.jpg)

If Unit Conversion is selected the user is presented with more selections to make, regarding the category of the units the user wishes to convert. Currently only Mass and Length conversions are available.
![Unit category screen](assets/README_screenshots/unit_category_screen_opti.jpg)

In both cases the user will be asked to input the currencies or the units that wishes to convert and the progrma auromatically will make the calculation using the Frankfurter API and the SymPy library.
![Value input and calculation](assets/README_screenshots/unit_conversion_screen_opti.jpg)

At the end of each conversion the user is asked if another conversion is needed or not. If yes, the user is taken to the initial selections between Currency and Unit conversions and if no, a Thank you message appears.
![End message screen](assets/README_screenshots/end_message_screen_opti.jpg)

## Features

#### Existing Features

   - Currency Conversion
![Currency calculation screen](assets/README_screenshots/currency_conversion_screen_opti.jpg)

   - Unit Conversion
      - Mass conversion
      - Length conversio
![Unit calculation screen](assets/README_screenshots/unit_conversion_screen_opti.jpg)

   - Input validation and error-checking
      - Conversions with the same values cannot be made
![Same value error message](assets/README_screenshots/same_values_error_opti.jpg)
![Same value error message](assets/README_screenshots/same_values_error_other_opti.jpg)
      - Where a number is required if a letter is insert will trigger an error message asking for the correct input
![Value error message](assets/README_screenshots/value_error_message_opti.jpg)
      - If a wrong selection is made or outside of the required range an error message appears asking for he correct input
![Error message](assets/README_screenshots/error_messages_opti.jpg)

#### Future Features

- More unit conversions they may be included (eg Time, Temperature, Area conversions)
- More tools can be offered (eg calculator, calendar)

## Data Model

The Data model used

## Testing

I have manually tested this project by doing the following:

  - Passed the code through a PEP8 linter and confirmer there are no problems
  - Extensively use the pogram making a lot of different combinations of inputs by inserting strings when numbers are expected, inserting the same value of units and selecting numbers out of bounds
  - Tested in my local terminal (VS Code) and the Code Institute Heroku terminal

## Bugs

Throughout my testing a few conversions would not work or return the expected value. That was because of typos in the code of the conversions, which were correct and the code functions as it suppose to.

## Validator Testing

- PEP8
  - No errors were returned from [PEP8online.com](https://pep8ci.herokuapp.com/) 
![PEP8 screnshot](assets/README_screenshots/PEP8_validator_opti.jpg)

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

  - Steps for deployment:
      - Fork or clone this repository
      - Create a new Heroku app
      - In the settings tap in the Heroku app inster in the Config Vars PORT as a key and 8000 as a value.
      - Set the buildbacks to Python and NodeJS in that order
      - Link the Heroku app to repository
      - Click on Deploy

## Credits

  - Code Institute for the deployment terminal
  - All validation checks for errors run with a <b><em>While</em></b> loop and use a try-except expression in their associated functions, which was taken from the [Love_Sandwiches project](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LS101+2021_T1/courseware/293ee9d8ff3542d3b877137ed81b9a5b/c92755338ef548f28cc31a7c3d5bfb46/) of the Code Institute LMS.
  - [Frankfurter API](https://www.frankfurter.app/docs/) for the currency conversion
  - [SymPy library](https://www.sympy.org/en/index.html) for providing the code for the conversions