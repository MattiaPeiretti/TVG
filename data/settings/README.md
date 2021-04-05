# Settings JSON file

Every data in the `settings.json` file will be automatically interpreted by the GUI settings page, as long as it meets al the necessary criteria.

## Sections

The settings must be divided in sections, like this: 

```json
//Settings.json
{
    "sections": [
        {
            "sectionName": "My section #1",
            "sectionSettings": [
                {
                    //Section settings...
                },
            ]
        },
        {
            "sectionName": "My section #2",
            "sectionSettings": [
                {
                    //Some other section settings...
                },
            ]
        },
    ]
}
```

## Putting settings inside a section

After creating and naming a section, you can proceed and add the settings.
You can do it like this:

```json
// Ouside section wrapper
{
    "title": "Example setting",
    "type": "select",
    "id":"MYSECTION_EXAMPLE_SETTING",
    "options": [
        "optionA",
        "optionB",
        "optionC"
    ],
    "default": "optionB",
    "description": "This is just a test setting for the parser"
},
// Other settings
```

## Section types:

Of course, for utility and UX purposes, there are different types of settings.

### Select
```json
// Ouside section wrapper
{
    "title": "Example setting",
    "id":"MYSECTION_EXAMPLE_SETTING",
    "type": "select",
    "options": [
        "optionA",
        "optionB",
        "optionC"
    ],
    "default": "optionB",
    "description": "This is just a test setting for the parser"
},
// Other settings
```

### Checkbox
```json
// Ouside section wrapper
{
    "title": "Example setting 2",
    "id":"MYSECTION_EXAMPLE_SETTING_CHECKBOX",
    "type": "checkbox",
    "option": "Do you want this option to be on?",
    "default": 1,
    "description": "This is just a test setting for the parser"
},
// Other settings
```

### Number
```json
// Ouside section wrapper
{
    "title": "Example setting 3",
    "id":"MYSECTION_EXAMPLE_SETTING_NUMBER",
    "type": "number",
    "min": 0,
    "max": 1,
    "default": 0,
    "description": "This is just a test setting for the parser"
},
// Other settings
```

## Full Example

```json
//Settings.json
{
    "sections": [
        {
            "sectionName": "My section #1",
            "sectionSettings": [
               {
                    "title": "Example setting",
                    "id":"MYSECTION_EXAMPLE_SETTING",
                    "type": "select",
                    "options": [
                        "optionA",
                        "optionB",
                        "optionC"
                    ],
                    "default": "optionB",
                    "description": "This is just a test setting for the parser"
                },
                {
                    "title": "Example setting 2",
                    "id":"MYSECTION_EXAMPLE_SETTING_CHECKBOX",
                    "type": "checkbox",
                    "option": "Do you want this option to be on?",
                    "default": 1,
                    "description": "This is just a test setting for the parser"
                },
                {
                    "title": "Example setting 3",
                    "id":"MYSECTION_EXAMPLE_SETTING_NUMBER",
                    "type": "number",
                    "min": 0,
                    "max": 1,
                    "default": 0,
                    "description": "This is just a test setting for the parser"
                },
            ]
        },
        {
            "sectionName": "My section #2",
            "sectionSettings": [
                {
                    //Some other section settings...
                },
            ]
        },
    ]
}
```
