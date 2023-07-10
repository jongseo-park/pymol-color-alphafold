from pymol import cmd


def coloraf(selection="all"):

    """
    AUTHOR
    Christian Balbin

    DESCRIPTION
    Colors Alphafold structures by pLDDT

    USAGE
    coloraf sele

    PARAMETERS

    sele (string)
    The name of the selection/object to color by pLDDT. Default: all
    """




    # modified
    # defind colorset
    cmd.set_color('n0', [0.051, 0.341, 0.827])
    cmd.set_color('n1', [0.416, 0.796, 0.945])
    cmd.set_color('n2', [0.996, 0.851, 0.212])
    cmd.set_color('n3', [0.992, 0.490, 0.302])

    # apply colorset
    cmd.color("n0", f"({selection}) and b > 90")
    cmd.color("n1", f"({selection}) and b < 90 and b > 70")
    cmd.color("n2", f"({selection}) and b < 70 and b > 50")
    cmd.color("n3", f"({selection}) and b < 50")


cmd.extend('plddt', coloraf)
cmd.auto_arg[0]['plddt'] = [cmd.object_sc, 'object', '']
