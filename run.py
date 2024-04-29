import typing
import json

from SpiffWorkflow.workflow import Workflow
from SpiffWorkflow.serializer.json import JSONSerializer
from SpiffWorkflow.bpmn.specs.bpmn_process_spec import BpmnProcessSpec
from SpiffWorkflow.bpmn.workflow import BpmnWorkflow
from SpiffWorkflow.camunda.parser.CamundaParser import CamundaParser
from SpiffWorkflow.camunda.specs.user_task import EnumFormField, UserTask
from SpiffWorkflow.util.task import TaskState
from SpiffWorkflow.task import Task

serializer = JSONSerializer()


def show_form(task: Task):
    form = task.task_spec.form
    if task.data is None:
        task.data = {}
    for field in form.fields:
        prompt = field.label
        if isinstance(field, EnumFormField):
            prompt += " (Auswahl: " + ', '.join(
                [str(option.id) for option in field.options]
            ) + ")"
        if field.type == "boolean":
            prompt += " (Auswahl: wahr, falsch)"
        prompt += " : "
        answer = input(prompt)
        if field.type == "long":
            answer = int(answer)
        if field.type == "boolean":
            answer = answer.lower().strip()
            answer = (answer == 'wahr' or answer == 'ja')
        task.set_data(**{field.id: answer})


def get_ready_tasks(workflow: BpmnWorkflow):
    # XXX Geht das auch einfacher?
    return workflow.get_tasks(state=TaskState.READY, manual=True)


parser = CamundaParser()
parser.add_bpmn_file('ducks.bpmn')
spec: BpmnProcessSpec = parser.get_spec('duck_process')
workflow: BpmnWorkflow = BpmnWorkflow(spec)

workflow.do_engine_steps()
ready_tasks: typing.List[Task | None] = get_ready_tasks(workflow)
while len(ready_tasks) > 0:
    for task in ready_tasks:
        if isinstance(task.task_spec, UserTask):
            show_form(task)
            # print(task.data)
        else:
            print("Complete Task ", task.task_spec.name)
        workflow.run_task_from_id(task.id)
        # ### Serialize ### Not working yet
        # data = workflow.serialize(serializer)
        # with open('workflow.json', 'w') as f:
        #     f.write(data)
        # with open('workflow.json') as fp:
        #     workflow_json = fp.read()
        #     workflow = Workflow.deserialize(serializer, workflow_json)

    workflow.do_engine_steps()
    ready_tasks: typing.List[Task | None] = get_ready_tasks(workflow)
# print(workflow.last_task.data)
