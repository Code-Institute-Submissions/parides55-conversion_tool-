
# ***CONVERSION TOOL***

<hr>

Conversion Tool is a Python terminal program, which runs in the Code Institute mock terminal on Heroku.

This program offers the opportunity to the user to make currency and unit conversions by using the Frankfurter API and the SymPy librrary. The Frankfurter API tracks the foreign exchange references rates published by the European Central Bank and the data refreshes around 16:00 CET every working day. The SymPy library offers the unit conversions based on the SI system and also many other scientific equations and calculations which are not part of this project.

Click here to use the program
<image>

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
  - [Deployment](#deployment)
  - [Credits](#credits)

</details>

## How to use it

<hr>

When the program first runs, it provides the user with some selections, where the user can choose what to convert, Currency or Units.
<image of the startup screen>

If Currency Conversion is selected immediately a list of all available currency codes is shown to clearly indicate to the user what codes can be selected.
<image of currency conversion>

If Unit Conversion is selected the user is presented with more selections to make, regarding the category of the units the user wishes to convert. Currently only Mass and Length conversions are available.
<image of the conversion categories>

In both cases the user will be asked to input the currencies or the units that wishes to convert and the progrma auromatically will make the calculation using the Frankfurter API and the SymPy library.



At the end of each conversion the user is asked if another conversion is needed or not. If yes, the user is taken to the initial selections between Currency and Unit conversions and if no, a Thank you message appears.
<image of the end message>

## Features

<hr>

### Existing Features

   - Currency Conversion
<image of the currency calculation>

   - Unit Conversion
      - Mass conversion
      - Length conversio
<image of the unit calculation>

   - Input validation and error-checking
      - Conversions with the same values cannot be made
<image same values message>
      - Where a number is required if a letter is insert will trigger an error message asking for the correct input
<image value error message>
      - If a wrong selection is made or outside of the required range an error message appears asking for he correct input
<image error message>

### Future Features

- More unit conversions they may be included (eg Time, Temperature, Area conversions)
- More tools can be offered (eg calculator, calendar)

## Data Model

<hr>
The Data model used

## Testing

<hr>

I have manually tested this project by doing the following:

  - Passed the code through a PEP8 linter and confirmer there are no problems
  - Extensively use the pogram making a lot of different combinations of inputs by inserting strings when numbers are expected, inserting the same value of units and selecting numbers out of bounds
  - Tested in my local terminal (VS Code) and the Code Institute Heroku terminal

## Bugs

<hr>

Throughout my testing a few conversions would not work or return the expected value. That was because of typos in the code of the conversions.

## Deployment

<hr>

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
  - All validation checks for errors run with a <em>While</em> loop and use a try-except expression in their associated functions, which was taken from the [Love_Sandwiches project](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LS101+2021_T1/courseware/293ee9d8ff3542d3b877137ed81b9a5b/c92755338ef548f28cc31a7c3d5bfb46/) of the Code Institute LMS.
  - [Frankfurter API](https://www.frankfurter.app/docs/) for the currency conversion
  - [SymPy library](https://www.sympy.org/en/index.html) for providing the code for the conversions