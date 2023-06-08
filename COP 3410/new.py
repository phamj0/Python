def counts(teamA, teamB):
    result = []
    for matches in teamB:
        count = 0
        for goals in teamA:
            if goals <= matches:
                count += 1
        result.append(count)
    return result