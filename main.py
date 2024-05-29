from CadastroEmpresa import CadastroEmpresa
from CadastroDepartamento import CadastroDepartamento
from CadastroCargo import CadastroCargo
from CadastroHorario import CadastroHorario
from CadastroFuncionario import CadastroFuncionario
from GeraLogs import GeraLogs

def run_and_log(cadastro, log):
    cadastro.run()
    console_output = GeraLogs.capturar_output()
    GeraLogs.salvar_arquivo(console_output, log)
    GeraLogs.limpar_e_fechar()

if __name__ == "__main__":
    GeraLogs.abrir_e_fechar()
    cadastro_empresa = CadastroEmpresa()
    run_and_log(cadastro_empresa, 'log_cadastro_empresa.txt')
    
    cadastro_departamento = CadastroDepartamento()
    run_and_log(cadastro_departamento, 'log_cadastro_departamento.txt')
    
    cadastro_cargo = CadastroCargo()
    run_and_log(cadastro_cargo, 'log_cadastro_cargo.txt')
    
    cadastro_horario = CadastroHorario()
    run_and_log(cadastro_horario, 'log_cadastro_horario.txt')
    
    cadastro_funcionario = CadastroFuncionario()
    run_and_log(cadastro_funcionario, 'log_cadastro_funcionario.txt')
