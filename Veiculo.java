class Automovel {
    String marca;
    int ano;
    boolean ligado;
    
    public Automovel(String marca, int ano) {
        this.marca = marca;
        this.ano = ano;
        this.ligado = false;
    }

    public void ligar() {
        if (!ligado) {
            ligado = true;
            System.out.println(marca + " foi ligado!");
        } else {
            System.out.println(marca + " ja esta ligado, não precisa ligar novamente!");
        }
    }

    public void desligar() {
        if (ligado) {
            ligado = false;
            System.out.println( marca + " foi desligado!");
        } else {
            System.out.println(marca + " já esta desligado, não precisa desligar!");
        }
    }
}

class Carro extends Automovel {
    float potencia;
    int marcha;
    String modelo;
    int velocidade;

    public Carro(String marca, int ano, float potencia, String modelo) {
        super(marca, ano);
        this.potencia = potencia;
        this.marcha = 0;
        this.modelo = modelo;
        this.velocidade = 0;
    }

    public void acelerar() {
        if (ligado) {
            velocidade += 5;
            if (velocidade < 20) {
                marcha = 1;
            } else if (velocidade < 40) {
                marcha = 2;
            } else if (velocidade < 60) {
                marcha = 3;
            } else if (velocidade < 80) {
                marcha = 4;
            } else if (velocidade < 220) {
                marcha = 5;
            } else if (velocidade > 220) {
                velocidade = 220;
            }
            System.out.println(modelo + " esta na " +marcha+ "ª marcha e "+ velocidade+"km/h");
        } else {
            System.out.println("O carro esta desligado por isso não pode acelerar!!!");
        }
    }
    public void reduzir() {
        if (ligado) {
            velocidade -= 5;
            if (velocidade < 0) {
                velocidade = 0;
                System.out.println("O carro esta na marcha Neutra e parado!!!");
            } else if (velocidade < 20) {
                marcha = 1;
            } else if (velocidade < 40) {
                marcha = 2;
            } else if (velocidade < 60) {
                marcha = 3;
            } else if (velocidade < 80) {
                marcha = 4;
            } else if (velocidade < 220) {
                marcha = 5;
            } else if (velocidade > 220) {
                velocidade = 220;
            }
            System.out.println(modelo + " esta na " +marcha+ "ª marcha e "+ velocidade+"km/h");
        } else {
            System.out.println("O carro esta desligado por isso não pode acelerar!!!");
        }
    }
}

class Moto extends Automovel {
    int cilindrada;
    int marcha;
    String modelo;
    int velocidade;

    public Moto(String marca, int ano, String modelo, int cilindrada) {
        super(marca, ano);
        this.modelo = modelo;
        this.cilindrada = cilindrada;
        this.velocidade = 0;
        this.marcha = 0;

    }

    public void acelerar() {
        if (ligado) {
            velocidade += 5;
            if (velocidade < 20) {
                marcha = 1;
            } else if (velocidade < 40) {
                marcha = 2;
            } else if (velocidade < 60) {
                marcha = 3;
            } else if (velocidade < 80) {
                marcha = 4;
            } else if (velocidade < 220) {
                marcha = 5;
            } else if (velocidade > 220) {
                velocidade = 220;
            }
            System.out.println(modelo + " esta na " +marcha+ "ª marcha e "+ velocidade+"km/h");
        } else {
            System.out.println("O veículo esta desligado por isso não pode acelerar!!!");
        }
    }
    public void reduzir() {
        if (ligado) {
            velocidade -= 5;
            if (velocidade < 0) {
                velocidade = 0;
                System.out.println("A moto esta na marcha Neutra e parada");
            } else if (velocidade < 20) {
                marcha = 1;
            } else if (velocidade < 40) {
                marcha = 2;
            } else if (velocidade < 60) {
                marcha = 3;
            } else if (velocidade < 80) {
                marcha = 4;
            } else if (velocidade < 220) {
                marcha = 5;
            } else if (velocidade > 220) {
                velocidade = 220;
            }
            System.out.println(modelo + " esta na " +marcha+ "ª marcha e "+ velocidade+"km/h");
        } else {
            System.out.println("A moto esta desligado por isso não pode acelerar!!!");
        }
    }
}

class Condutor {
    String nome;
    String habilitacao; 
    Automovel veiculo; 

    public Condutor(String nome, String habilitacao) {
        this.nome = nome;
        this.habilitacao = habilitacao;
        this.veiculo = null;
    }

    public void subirMoto(Moto moto) {
        if (this.habilitacao == "A" || this.habilitacao == "A&B") {
            if (this.veiculo == null) {
                this.veiculo = moto;
                System.out.println(this.nome + " subiu na moto " + moto.modelo);
            } else {
                System.out.println(this.nome + " Já estava em um veículo, então ele trocou e subiu na moto " + moto.modelo);
                this.veiculo = moto;
            }
        } else {
            System.out.println(this.nome + " não possui habilitação na categoria A para pilotar moto!");
        }
    }

    public void entrarNoCarro(Carro carro) {
        if (this.habilitacao == "B" || this.habilitacao == "A&B") {
            if (this.veiculo == null) {
                this.veiculo = carro;
                System.out.println(this.nome + " entrou no carro " + carro.modelo);
            } else {
                System.out.println(nome + " Já estava em um veículo, então ele trocou de veículo e entrou no carro " + carro.modelo);
                this.veiculo = carro;
            }
        } else {
            System.out.println(nome + " não possui habilitação na categoria B para dirigir carro!");
        }
    }

    public void ligarVeiculo() {
        if (this.veiculo != null) {
            this.veiculo.ligar();
        } else {
            System.out.println("O condutor não está conduzindo nenhum veículo no momento.");
        }
    }

    public void desligarVeiculo() {
        if (this.veiculo != null) {
            this.veiculo.desligar();
        } else {
            System.out.println("O condutor não está conduzindo nenhum veículo no momento.");
        }
    }

    public void acelerar() {
        if (this.veiculo != null) {
            if (this.veiculo.ligado) {
                if (this.veiculo instanceof Carro) {
                    ((Carro) this.veiculo).acelerar();
                } else if (this.veiculo instanceof Moto) {
                    ((Moto) this.veiculo).acelerar();
                }
            } else {
                System.out.println("O veículo está desligado, não pode acelerar!");
            }
        } else {
            System.out.println("O condutor não está conduzindo nenhum veículo no momento.");
        }
    }

    public void reduzir() {
        if (this.veiculo != null) {
            if (this.veiculo.ligado) {
                if (this.veiculo instanceof Carro) {
                    ((Carro) this.veiculo).reduzir();
                } else if (this.veiculo instanceof Moto) {
                    ((Moto) this.veiculo).reduzir();
                }
            } else {
                System.out.println("O veículo está desligado, não pode reduzir a velocidade!");
            }
        } else {
            System.out.println("O condutor não está conduzindo nenhum veículo no momento.");
        }
    }
}

public class Dirigir {
    public static void main(String[] args) {

        Carro auto = new Carro("Fiat", 1990, 1.0f, "Uno");
        Moto moto = new Moto("Factor", 1000, "GS-092", 300);
        Condutor motorista1 = new Condutor("Gabriel", "A&B");
        Condutor motorista2 = new Condutor("Guilherme", "B");
    
        motorista1.entrarNoCarro(auto);
        motorista1.ligarVeiculo();
        for (int i = 0; i < 5; i++) {
            motorista1.acelerar();
        }
        motorista1.desligarVeiculo();

        System.out.println("====================================================");

        motorista2.subirMoto(moto);
        for (int i = 0; i < 5; i++) {
            motorista1.acelerar();
        }
        motorista2.desligarVeiculo();
    }
}
