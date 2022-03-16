import sys
import json


def DFS(item, values):

    if 'value' in item.keys():
        val_ind = next((i for i, x in enumerate(values) if x['id'] == item['id']), False)
        if val_ind is not False:
            item['value'] = values[val_ind]['value']

    if 'values' in item.keys():
        for successor in item['values']:
            DFS(successor, values)


def main():

    with open(sys.argv[1], "r") as tasks_json:
        with open(sys.argv[2], "r") as values_json:

            values = json.load(values_json)['values']
            report = json.load(tasks_json)['tests']

            for i in range(len(report)):
                DFS(report[i], values)

            with open("report.json", "w") as report_file:
                json.dump(report, report_file)


if __name__ == '__main__':
    main()