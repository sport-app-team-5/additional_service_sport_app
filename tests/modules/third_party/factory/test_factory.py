from app.modules.third_party.infrastructure.repository import (ThirdPartyRepositoryPostgres)
from app.modules.third_party.domain.repository import (ThirdPartyRepository)

from app.modules.third_party.infrastructure.factories import RepositoryFactory


def test_create_object_third_party_repository():
    factory = RepositoryFactory()
    repo = factory.create_object(ThirdPartyRepository)
    assert isinstance(repo, ThirdPartyRepositoryPostgres)