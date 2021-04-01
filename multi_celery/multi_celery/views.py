from rest_framework.views import APIView
from rest_framework.response import Response
from celery.result import AsyncResult

from .tasks import factorial, dictionary, lst

task_map = {
    'factorial': factorial,
    'dictionary': dictionary,
    'lst': lst
}


def get_result(task_id):
    return AsyncResult(task_id)


class TaskView(APIView):
    def post(self, request):
        task = task_map[request.data['task']]
        arguments = request.data['arguments']
        result = task.delay(arguments)
        return Response(data={'task_id': result.id})


class ResultView(APIView):
    def get(self, request, task_id):
        task_result = get_result(task_id)
        status, result = task_result.status, task_result.result
        return Response(data={'status': status, 'result': str(result)})
