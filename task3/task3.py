import sys
import json
import copy



def main():

    with open(sys.argv[1], "r") as tasks_json:
        with open(sys.argv[2], "r") as values_json:
            data = json.load(tasks_json)
            values = json.load(values_json)

            report = copy.deepcopy(data['tests'])

            print(values['values'])

            # for i in range(len(data['tests'])):
            #
            #     data_item = data['tests'][i]
            #     report_item = report[i]
            #
            #     report_item['value'] = values_item["id"]



            # print(data)
            # print(data["tests"][0])


            # report = open("report.json", "x")


if __name__ == '__main__':
    main()