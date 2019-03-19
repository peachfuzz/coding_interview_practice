from project import Project


def orderDep(files, deps):
    projects = []
    # for each filename in files, create a project object
    for f in files:
        new_project = Project(f)
        projects.append(new_project)

    # for each project object, add its deps.
    for dep in deps:
        name = dep[0]
        depp = dep[1]
        for project in projects:
            if project.filename == name:
                project.add_dependency(depp)

    # order the project objects by dependencies
    ordered_projects = []
    first_projects = []
    last_projects = []
    for proj in projects:

        if proj.dependencies == []:
            first_projects.append(proj)
        else:
            # sort by dependencies
            last_projects.append(proj)

    ordered_projects = first_projects + last_projects
    # binary_search_recur(ordered_projects)
    # return the filenames of the project objects
    return [project.filename for project in ordered_projects]


def binary_search_recur(items):
    #     if len(arr) > 1:
    #         mid = len(arr) // 2  # Finding the mid of the array
    #         L = arr[:mid]  # Dividing the array elements
    #         R = arr[mid:]  # into 2 halves

    #         mergeSort(L)  # Sorting the first half
    #         mergeSort(R)  # Sorting the second half

    #         i = j = k = 0

    #         # Copy data to temp arrays L[] and R[]
    #         while i < len(L) and j < len(R):
    #             if L[i] < R[j]:
    #                 arr[k] = L[i]
    #                 i += 1
    #             else:
    #                 arr[k] = R[j]
    #                 j += 1
    #             k += 1

    #         # Checking if any element was left
    #         while i < len(L):
    #             arr[k] = L[i]
    #             i += 1
    #             k += 1

    #         while j < len(R):
    #             arr[k] = R[j]
    #             j += 1
    #             k += 1

    #     length = len(items)
    #     if length % 2 == 0:
    #         half = length / 2
    #     else:
    #         half = (length - 1) / 2

    first_half, second_half = a_list[: half + 1], a_list[half:]
    return binary_search_recur(first_half + second_half)
