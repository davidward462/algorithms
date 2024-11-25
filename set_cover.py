
# Given points which are contained in some number of sets, determine the smallest set of sets which covers all points.
# Arguments:
#       sets -> the sets which contain the points in question. This is a dictionary of sets.
#       points_needed -> all the points we want to cover. This is a set.
def setCover(sets, points_needed):
        final_sets = set()

        # while points_needed is not empty
        while points_needed:
                best_set = None
                points_covered = set()

                # for each set and its associated points in 'sets'
                for s, points in sets.items():
                        covered = points_needed & points # set intersection

                        if len(covered) > len(points_covered):
                                # we cover more points with the addition of the new set
                                best_set = s
                                points_covered = covered

                # remove the points we have covered
                points_needed -= points_covered # set difference
                final_sets.add(best_set)

        return final_sets
