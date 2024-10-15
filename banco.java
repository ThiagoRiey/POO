import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Banco {
    private String nome;
    private double saldo;
    private String senha;

    public Banco(String nome) {
        this.nome = nome;
        this.saldo = 0;
        this.senha = null;
    }

    public void cadastrarSenha() {
        if (senha == null) {
            Scanner scanner = new Scanner(System.in);
            System.out.print("Cadastrar sua senha: ");
            this.senha = scanner.nextLine();
            System.out.println("Senha cadastrada com sucesso!");
        } else {
            System.out.println("Senha já cadastrada.");
        }
    }

    public boolean verificarSenha() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite sua senha: ");
        String tentativa = scanner.nextLine();
        return tentativa.equals(senha);
    }

    public void depositar(double valor) {
        if (valor > 0) {
            this.saldo += valor;
            System.out.printf("Depósito de R$%.2f realizado com sucesso%n", valor);
        } else {
            System.out.println("Valor de depósito inválido.");
        }
    }

    public void consultarSaldo() {
        System.out.printf("Saldo atual: R$%.2f%n", this.saldo);
    }

    public void apresentar() {
        System.out.printf("Cliente: %s, Saldo: R$%.2f%n", this.nome, this.saldo);
    }

    public void transferir(Banco destinatario, double valor) {
        if (this.saldo >= valor && valor > 0) {
            if (verificarSenha()) {
                this.saldo -= valor;
                destinatario.saldo += valor;
                System.out.printf("Transferência de R$%.2f realizada para %s.%n", valor, destinatario.nome);
            } else {
                System.out.println("Senha incorreta. Transferência cancelada.");
            }
        } else {
            System.out.println("Transferência inválida. Saldo insuficiente ou valor incorreto.");
        }
    }

    public static Banco criarConta() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite o seu nome: ");
        String nome = scanner.nextLine();
        Banco cliente = new Banco(nome);
        cliente.cadastrarSenha();
        return cliente;
    }

    public static Banco selecionarConta(List<Banco> clientes) {
        if (clientes.isEmpty()) {
            System.out.println("Nenhuma conta disponível. Crie uma conta primeiro.");
            return null;
        }

        System.out.println("=== Selecionar Conta ===");
        for (int i = 0; i < clientes.size(); i++) {
            System.out.printf("%d. %s%n", i + 1, clientes.get(i).nome);
        }

        Scanner scanner = new Scanner(System.in);
        System.out.print("Escolha o número da conta: ");
        int opcao = scanner.nextInt();
        if (opcao >= 1 && opcao <= clientes.size()) {
            return clientes.get(opcao - 1);
        } else {
            System.out.println("Opção inválida.");
            return null;
        }
    }

    public static void main(String[] args) {
        List<Banco> clientes = new ArrayList<>();
        Banco clienteSelecionado = null;

        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("=== Menu do Banco ===");
            System.out.println("1. Criar Conta");
            System.out.println("2. Selecionar Conta");
            System.out.println("3. Depositar");
            System.out.println("4. Consultar saldo");
            System.out.println("5. Apresentar dados");
            System.out.println("6. Transferir");
            System.out.println("7. Sair");

            System.out.print("Escolha uma opção: ");
            String opcao = scanner.nextLine();
            switch (opcao) {
                case "1":
                    Banco novoCliente = Banco.criarConta();
                    clientes.add(novoCliente);
                    break;
                case "2":
                    clienteSelecionado = Banco.selecionarConta(clientes);
                    break;
                case "3":
                    if (clienteSelecionado != null) {
                        System.out.print("Informe o valor para depósito: ");
                        double valor = scanner.nextDouble();
                        scanner.nextLine();  // Limpa o buffer
                        clienteSelecionado.depositar(valor);
                    } else {
                        System.out.println("Você precisa selecionar uma conta primeiro!");
                    }
                    break;
                case "4":
                    if (clienteSelecionado != null) {
                        clienteSelecionado.consultarSaldo();
                    } else {
                        System.out.println("Você precisa selecionar uma conta primeiro!");
                    }
                    break;
                case "5":
                    if (clienteSelecionado != null) {
                        clienteSelecionado.apresentar();
                    } else {
                        System.out.println("Você precisa selecionar uma conta primeiro!");
                    }
                    break;
                case "6":
                    if (clienteSelecionado != null) {
                        System.out.print("Informe o nome do destinatário: ");
                        String nomeDestinatario = scanner.nextLine();
                        Banco destinatario = null;

                        for (Banco cliente : clientes) {
                            if (cliente.nome.equals(nomeDestinatario)) {
                                destinatario = cliente;
                                break;
                            }
                        }

                        if (destinatario != null) {
                            System.out.print("Informe o valor para transferência: ");
                            double valorTransferencia = scanner.nextDouble();
                            scanner.nextLine();  // Limpa o buffer
                            clienteSelecionado.transferir(destinatario, valorTransferencia);
                        } else {
                            System.out.println("Destinatário não encontrado.");
                        }
                    } else {
                        System.out.println("Você precisa selecionar uma conta primeiro!");
                    }
                    break;
                case "7":
                    System.out.println("Saindo do sistema...");
                    return;
                default:
                    System.out.println("Opção inválida.");
                    break;
            }
        }
    }
}
