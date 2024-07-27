from pathlib import Path

from k8grep.k8grep import stream_objects_from_dir


def test_stream_objects_from_dir():
   res = tuple(stream_objects_from_dir(Path(__file__).parent.joinpath('simple-app')))

   assert len(res) == 3

   for obj in res:
      assert 'kind' in obj

   res = sorted(res, key= lambda o: o['kind'])

   assert res[0]['kind'] == 'Deployment'
   assert res[1]['kind'] == 'Ingress'
   assert res[2]['kind'] == 'Service'
