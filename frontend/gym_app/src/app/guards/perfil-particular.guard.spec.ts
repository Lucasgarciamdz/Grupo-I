import { TestBed } from '@angular/core/testing';
import { CanActivateFn } from '@angular/router';

import { PerfilParticularGuard } from './perfil-particular.guard';

describe('perfilParticularGuard', () => {
  const executeGuard: CanActivateFn = (...guardParameters) => 
      TestBed.runInInjectionContext(() => PerfilParticularGuard(...guardParameters));

  beforeEach(() => {
    TestBed.configureTestingModule({});
  });

  it('should be created', () => {
    expect(executeGuard).toBeTruthy();
  });
});
