# Azure DevOps - code coverage report

## Usage
``
run.py --organization-url https://dev.azure.com/your_organization --project-name "Project Name" --token 24yu2y34gu23 --definition-regex "(^\\base_services\\|^\\custom_services\\)" --branch-name v1.2.0
``

or

``
run.py -o https://dev.azure.com/your_organization -p "Project Name" -t 24yu2y34gu23 -d "(^\\base_services\\|^\\custom_services\\)" -b v1.2.0
``

#### Parameters
`--organization-url` parameter is required

`--project-name` parameter is required

`--token access_token` parameter is required

`--definition-regex` parameter is optional. It's used to match build definition full path which contains build definition path and build definition name joined with `\` (backslash) character. For instance, if the build definition name is `customer_service` and it's in folder `\base_services\common\` then the full path is `\base_services\common\customer_service`.

`--branch-name` parameter is optional. Default value: `master`
