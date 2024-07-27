from pathlib import Path

import pytest

from k8grep.k8grep import stream_objects_from_cmd, stream_objects_from_dir


def test_stream_objects_from_dir():
   res = tuple(stream_objects_from_dir(Path(__file__).parent.joinpath('simple-app')))

   assert len(res) == 3

   for obj in res:
      assert 'kind' in obj

   res = sorted(res, key= lambda o: o['kind'])

   assert res[0]['kind'] == 'Deployment'
   assert res[0]['metadata']['name'] == 'simple-app'
   assert res[1]['kind'] == 'Ingress'
   assert res[1]['metadata']['name'] == 'simple-app'
   assert res[2]['kind'] == 'Service'
   assert res[2]['metadata']['name'] == 'simple-app-service'

@pytest.mark.parametrize("file,expected_obj", (
   (
      str(Path(__file__).parent.joinpath('simple-app').joinpath('simple-app-deployment.yaml')),
      {'kind': 'Deployment',
       'metadata': {
         'name': 'simple-app'
       },
      }
   ),
   (
      str(Path(__file__).parent.joinpath('simple-app').joinpath('simple-app-ingress.yaml')),
      {'kind': 'Ingress',
       'metadata': {
         'name': 'simple-app'
       },
      }
   ),
   (
      str(Path(__file__).parent.joinpath('simple-app').joinpath('simple-app-service.yaml')),
      {'kind': 'Service',
       'metadata': {
         'name': 'simple-app-service'
       },
      }
   ),
   )
)
def test_stream_objects_from_cmd_single_obj(file, expected_obj):

   res = tuple(stream_objects_from_cmd(f'cat {file}'))
   assert len(res) == 1

   obj = res[0]

   assert 'kind' in obj
   assert obj['kind'] == expected_obj['kind']
   assert obj['metadata']['name'] == expected_obj['metadata']['name']


def test_stream_objects_from_cmd():
   res = tuple(stream_objects_from_cmd(f"kustomize build {Path(__file__).parent.joinpath('ldap').joinpath('base')}"))

   assert len(res) == 3

   for obj in res:
      assert 'kind' in obj

   res = sorted(res, key= lambda o: o['kind'])
