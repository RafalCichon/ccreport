import logging

from ..utils.bytes_utils import BytesUtils
from ..utils.zip_utils import ZipUtils

logger = logging.getLogger(__name__)


class ArtifactContentReader:
    def __init__(self, build_client):
        self.__build_client = build_client

    def read(self, project_name, build, artifact_name, entry_paths):
        logger.info(
            'Reading the contents from the \'{artifactName}\' artifact.'
            .format(artifactName=artifact_name))
        artifact_content = self.__get_artifact_content(project_name, build, artifact_name)
        entry_content = None
        for path in entry_paths:
            entry_content = ArtifactContentReader.__read_entry_content(artifact_content, path)
            if entry_content:
                break
        return entry_content

    def __get_artifact_content(self, project_name, build, artifact_name):
        content_chunks = self.__build_client.get_artifact_content_zip(
            project_name,
            build.id,
            artifact_name
        )
        return BytesUtils.join_chunks(content_chunks)

    @staticmethod
    def __read_entry_content(content, entry_path):
        entry_content = ZipUtils.read_entry_content(content, entry_path)
        if not entry_content:
            logger.warning('The \'{entryPath}\' entry not found.'.format(entryPath=entry_path))
            return None
        if entry_content == '':
            logger.warning('The \'{entryPath}\' entry is empty.'.format(entryPath=entry_path))
            return None
        logger.info('The \'{entryPath}\' entry was found with none empty content.'.format(entryPath=entry_path))
        return entry_content
