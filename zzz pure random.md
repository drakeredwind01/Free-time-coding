should we properly categorize our branches?

my mentor says it might be a good idea to incorporate common practice branch grouping
```bash
bugfix/no_destination_for_href
feature/adding_picture_of_a_cute_puppy
release/cute_puppy_update_for_better_retention
hotfix/corrupt_image_breaks_the_site_fix
```
for example:
```bash
git checkout -b feature/36-add-new-iam-user-drakeredwind01
instead of
git checkout -b 36-add-new-iam-user-drakeredwind01
```
doing this would make finding specific branches much easier as each prefaced catagory would show as another folder with all concerning branches within.
```bash
HFLA
├───bugfix
│   ├───css_is_broken_on_home_page
│   └───no_destination_for_href
├───feature
│   └───adding_picture_of_a_cute_puppy
├───release
│   └───cute_puppy_update_for_better_retention
├───hotfix
│   └───corrupt_image_breaks_the_site_fix
├───iam_users
│   └───every_thing_is_on_on_fire_help
└───admin
    └───sigh
```
can also add features such as admin, iam_users, etc.
this is a standard used in most places
in accordance with [atlassian.com](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)

| branch  | how to incorperate | notes                                                                |
|---------|--------------------|----------------------------------------------------------------------|
| bugfix: | [bugfix/]          | problem that should be fixed that doesn't add any new functionality  |
| Feature | [feature/]         | an attribute or characteristic that adds value to the product.       |
| Release | [release/]         | where the maintainers believe the software is worth trying and using |
| Hotfix  | [hotfix/]          | should never use. needs to be added right away into production       |
