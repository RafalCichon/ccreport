import logging

logger = logging.getLogger(__name__)


class ArtifactReader:
    def __init__(self, build_client):
        self.__build_client = build_client

    def get_code_coverage_artifact(self, project_name, build):
        logger.info(
            'Searching for code coverage artifact in the \'{buildNumber}\' build.'
            .format(buildNumber=build.build_number)
        )
        artifacts = self.__build_client.get_artifacts(project_name, build.id)
        artifact_name = 'Code Coverage Report_' + str(build.id)
        artifact = next((x for x in artifacts if x.name == artifact_name), None)
        if artifact:
            logger.info(
                'Code coverage artifact found in the \'{buildNumber}\' build.'
                ' Artifact name: \'{artifactName}\''
                .format(buildNumber=build.build_number,
                        artifactName=artifact.name)
            )
        else:
            logger.warning(
                'Code coverage artifact \'{artifactName}\' not found in the \'{buildNumber}\' build.'
                .format(artifactName=artifact_name,
                        buildNumber=build.build_number)
            )
        return artifact
