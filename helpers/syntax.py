
def get_sidecar_blf_syntax(line: int, value, label):
    ignore_values = [None, "", "-"]
    if value in ignore_values:
        return
    else:
        syntax = ["",
        f"expansion_module.1.key.{line}.label = {label}",
        f"expansion_module.1.key.{line}.line = 1",
        f"expansion_module.1.key.{line}.type = 16",
        f"expansion_module.1.key.{line}.value = {value}"]
        return syntax

def get_deskphone_blf_syntax(line: int, value, label):
    ignore_values = [None, "", "-"]
    if value in ignore_values:
        return
    else:
        syntax = ["",
        f"linekey.{line}.label = {label}",
        f"linekey.{line}.line = 1",
        f"linekey.{line}.type = 16",
        f"linekey.{line}.sub_type = blf",
        f"linekey.{line}.value = {value}"]
        return syntax
