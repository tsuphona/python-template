Placeholder for necessary submodules
or third-party libraries, use the following command
to add new submodule

```bash
git submodule add https://github.com/project/project.git vendors
```
The command above will add a submodule from the specified
git repository under the name `vendors`.

After this we have to run

```bash
git submodule update --init --recursive
```
