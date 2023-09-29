import { TestBed } from '@angular/core/testing';
import { CanActivateFn } from '@angular/router';

import { AuthsessionGuard } from './authsession.guard';

describe('authsessionGuard', () => {
  const executeGuard: CanActivateFn = (...guardParameters) => 
      TestBed.runInInjectionContext(() => AuthsessionGuard(...guardParameters)); //No se porque da error

  beforeEach(() => {
    TestBed.configureTestingModule({});
  });

  it('should be created', () => {
    expect(executeGuard).toBeTruthy();
  });
});
