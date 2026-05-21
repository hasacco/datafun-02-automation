# Data Analytics Fundamentals

This site provides documentation for this project.
Use the navigation to explore module-specific materials.

## How-To Guide

Many instructions are common to all projects.
See [⭐ **Workflow: Apply Example**](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
to get this project running on your machine.

## Project Materials

- [project-instructions](./project-instructions.md)
- [your-files](./your-files.md)
- [module](./module/index.md)
- [glossary](./glossary.md)
- [api](./api.md)

## Custom Project - Grade Reporting

### Dataset
I used a data set that I could obtain in my classroom. For program testing purposes, test scores and students were created.
The data set I would use when applying this program in my classroom would be an actual set of test scores from my Algebra classes.

### Signals
I did not create any signals for this project.

### Experiments
I worked through each function separately, making changes and then running the program to test what I had changed. After I got one part of the function working, I would add an additional step into the loop. Initially, I was initially only printing information into one .txt file at a time, but found that using a nested if loop, I could post into one file each time and one file only when certain criteria were met. I experimented with testing values to make sure the correct type of value was input by the user so that the program would not produce errors and terminate, but was unsuccessful in my experimentation. Currently, my program has no way to handle an incorrect input type except terminating, but I plan on continuing to experiment with this concept in order to prevent termination and instead re-prompt the user for an input of the correct type before continuing through the program.

### Results
I observed that I was able to create .txt files that were useful in an educational setting, allowing the user to input available data for students in order to classify students according to specified criteria. I do think I could have simplified the program and not created all the files that I did, but I was trying to maintain use of the 4 types of functions in the original program.

### Interpretation
I can see that this would be especially useful in the educational setting if I was able to make the program read a data file and classify students for a teacher without needing manual input of scores. I also see that this could be applicable to many fields - sports (i.e. race times, powerlifting), medical (i.e. blood test values tracked over time, patients who need monitoring based on values), real estate (i.e. market values in different years, flags for unusually high/low values), etc.
