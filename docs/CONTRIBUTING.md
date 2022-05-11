# Contribute to LibreNMS Handler

Thank you for wanting to contribute to the project!
`librenms_handler` has no complex logic behind it - all you need to do is read the [API docs](https://docs.librenms.org/API/) and follow the existing code structure.

When you are ready to create a pull request for your contributions, please pull them into the `stage` branch, **not** `main`.
Merging into stage allows me to test the code before officially including it in the PyPI package.

Alongside the documentation, there are the following design considerations to follow when contributing.

## Adding new features

When adding new functions and endpoints, please search for their tracked [issues](https://github.com/WhaleJ84/librenms_handler/issues) first and include the relevant issue number in your commit.
If the issue does not exist yet, please open a new issue with the function name as the title, and apply the **enhancement** label before making the commit. No worries if the issue numbers are not included in the commit; they can be tagged in the pull request instead.

## Design Decisions

By following these standards, the code should be easy for people from all skill-sets to help out!

- When the official documentation is inconsistent, follow the levels of documentation provided in the docstrings of existing functions. It is better to provide more information to the user than following the mistakes of the documentation.
- All submissions are subject to a [PyLint](https://github.com/PyCQA/pylint) test upon submission. Linting the code checks for [PEP8](https://pep8.org/) compliance and improves readability. While not all recommendations are reasonable to follow, try to meet them where applicable.
- To make the code consistent and clear to read, I recommend you run [Black](https://github.com/psf/black) on your code before submitting. You may not agree with the way it formats the code, but by keeping the consistency, it's easier for others to follow by example.

Adhering to these standards are not mandatory, but if they are not included in the pull request, I will be making the changes myself at a later date.
