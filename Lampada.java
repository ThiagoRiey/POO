public class lampada {
    private String marca;
    private String modelo;
    private boolean ligada;
    private double potencia;

   
    public lampada(String marca, String modelo, double potencia) {
        this.marca = marca;
        this.modelo = modelo;
        this.potencia = potencia;
        this.ligada = false; 
    }

    
    public void ligar() {
        if (potencia > 100) {
            System.out.println("A lâmpada queimou! Potência excessiva.");
        } else if (potencia > 0) {
            this.ligada = true;
            System.out.println("A lâmpada está ligada.");
        } else {
            System.out.println("Não é possível ligar a lâmpada com potência menor ou igual a 0.");
        }
    }

    
    public void desligar() {
        if (ligada) {
            this.ligada = false;
            System.out.println("A lâmpada está desligada.");
        } else {
            System.out.println("A lâmpada já está desligada.");
        }
    }

    
    public boolean isLigada() {
        return ligada;
    }

   
    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public double getPotencia() {
        return potencia;
    }

    public void setPotencia(double potencia) {
        this.potencia = potencia;
    }
    
    
    public static void main(String[] args) {
        lampada lampada = new lampada("Philips", "XYZ123", 80);
        lampada.ligar(); 
        lampada.desligar(); 
    }
}
