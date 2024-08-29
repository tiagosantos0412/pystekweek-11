document.getElementById('cadastroForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Evita o envio do formulário

    var senha = document.getElementById('senha').value;
    var confirmaSenha = document.getElementById('confirmaSenha').value;
    var mensagemErro = document.getElementById('mensagemErro');

    if (senha  confirmaSenha) {
        mensagemErro.textContent = "As senhas não coincidem!";
        mensagemErro.style.display = 'block';
    } else {
        mensagemErro.style.display = 'none';
        // Se as senhas coincidirem, aqui você pode enviar o formulário, ou processar os dados
        alert("Cadastro realizado com sucesso!");
        // document.getElementById('cadastroForm').submit(); // Enviar o formulário
    }
});
