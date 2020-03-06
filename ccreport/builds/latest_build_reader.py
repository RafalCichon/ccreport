import logging

from azure.devops.exceptions import AzureDevOpsServiceError

logger = logging.getLogger(__name__)


class LatestBuildReader:
    __default_branch_name = 'master'

    def __init__(self, build_client):
        self.__build_client = build_client

    def read(self, project_name, definition, branch_name):
        branch_name = branch_name or LatestBuildReader.__default_branch_name
        logger.info(
            'Searching for the latest build for the \'{definitionName}\' build definition (branch: {branchName}).'
            .format(definitionName=definition.name, branchName=branch_name)
        )
        try:
            latest_build = self.__build_client.get_latest_build(
                project_name,
                definition.id,
                branch_name)
        except AzureDevOpsServiceError as e:
            logger.warning(e.message)
            logger.warning(
                'The latest build not found for the \'{definitionName}\' build definition (branch: {branchName}).'
                .format(definitionName=definition.name, branchName=branch_name)
            )
            return None
        else:
            logger.info(
                'The latest build found for the \'{definitionName}\' build definition (branch: {branchName}).'
                ' Build number: \'{buildNumber}\''
                .format(definitionName=definition.name, branchName=branch_name, buildNumber=latest_build.build_number)
            )
        return latest_build
