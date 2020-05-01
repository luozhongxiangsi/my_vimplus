def Settings(**kwargs):
    client_data = kwargs['client_data']
    return {
        'iterpreter_path': client_data['g:ycm_pathon_interpreter_path'],
        'sys_path': client_data['g:ycm_pathon_sys_path']
    }
