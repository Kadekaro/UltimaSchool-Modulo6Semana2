from django import forms


class inscreverContato(forms.Form):
    nome = forms.CharField(label="Nome: ")
    email = forms.EmailField(label="Email: ")
    telefone = forms.IntegerField(label="Telefone: ", widget=forms.TextInput)


class reservarBanho(forms.Form):
    nome_pet = forms.CharField(label="Nome do Pet: ")
    telefone = forms.CharField(label="Telefone de Contato: ", widget=forms.TextInput)
    data = forms.DateField(label="Data da Reserva: ")
    observacao = forms.CharField(label="Observação: ", widget=forms.Textarea)
