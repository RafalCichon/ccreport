import re
import logging

logger = logging.getLogger(__name__)


class BuildDefinitionsFilter:
    @staticmethod
    def filter(definitions, build_definition_pattern):
        if not build_definition_pattern:
            return definitions
        logger.info('Filtering build definitions using regular expression: ' + build_definition_pattern)
        compiled_pattern = re.compile(build_definition_pattern)
        result = []
        for d in definitions:
            full_path = d.path + '\\' + d.name
            if not compiled_pattern.match(full_path):
                continue
            result.append(d)
        return result
