# ccreport - code coverage report

## Installation
`pip install ccreport`

## Usage
`
ccreport -o https://dev.azure.com/your_organization -p "Project Name" -t 24yu2y34gu23 -d "(^\\base_services\\|^\\custom_services\\)" -b v1.2.0
`

#### Parameters
`-o/--organization-url` parameter is required

`-p/--project-name` parameter is required

`-t/--token` parameter is required

`-d/--definition-regex` parameter is optional. It's used to match build definition full path which contains build definition path and build definition name joined with `\` (backslash) character. For instance, if the build definition name is `customer_service` and it's in folder `\base_services\common\` then the full path is `\base_services\common\customer_service`.

`-b/--branch-name` parameter is optional. Default value: `master`
