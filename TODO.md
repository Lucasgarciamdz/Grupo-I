# TODO Program1

## General

- [ ] Se desaparecio el boton de editar perfil!!. Revisar el ngif.
""" html
<app-navbar></app-navbar>
<div class="container">
    <div class="d-flex flex-column align-items-center mb-2">
        <app-profile-picture [image]="'../../assets/default-profile-picture.jpeg'" [name]="profileName"></app-profile-picture>
        <app-edit-profile-btn *ngIf="currentUser == profileId"></app-edit-profile-btn>
    </div>
    <div class="d-flex justify-content-between mb-4">
        <app-profile-stats-box [label]="'Height'" [number]="height"></app-profile-stats-box>
        <app-profile-stats-box [label]="'Weight'" [number]="weight"></app-profile-stats-box>
        <app-profile-stats-box [label]="'Age'" [number]="age"></app-profile-stats-box>
      </div>
    <div class="d-flex flex-column mb-4">
        <app-account-info></app-account-info>
    </div>
    <div class="d-flex flex-column mb-4">
        <app-notifications-box></app-notifications-box>
    </div>
    <app-navbar-responsive></app-navbar-responsive>
</div>
"""
- [ ] Manejar el envio de mails. (backend)
- [ ] Mejorar el register. (backend)

## Alumno

### Planificaciones

- [ ] Posibilidad de darse de baja. LISTO
- [ ] Si ya esta inscripto, que no le salga el boton de join (o que se transforme en darse de baja). LISTO
- [ ] Pulir stud-workout (home alumno). LISTO
- [ ] Hacer andar y pulir views/planificacion. 

### Clases

- [ ] Mejorar la vista de clases para el alumno. Que se vea mas bonito. (views/class). **Instalar ng add @angular/material**. LISTO

## Profesor

- [ ] Posibilidad de dar una clase. El admin debe recibir un mail para aprobarla.
- [ ] Chequear certificacion del profe a la hora de dar la clase.
- [ ] Mejorar perfil profesor.

## HOME

- [ ] Hay que mejorar los caruseles, hacer que funcionen random o posta. LISTO
- [ ] Posibilidad de ver todas las clases. EN PROCESO
- [ ] Arreglar search bar para buscar clases. (segun tipo clase). EN PROCESO
  - [ ] Deberia mostrar una lista de clases que coincida con la busqueda (nueva view). Hacer un carrusel vertical que tambien sirva para ver todas las clases. Recibe una lista de clases.

## Admin

- [ ] Aprobar profe clase.
- [ ] Mejorar el dar de alta.