import { TestBed } from '@angular/core/testing';
import { CanActivateFn } from '@angular/router';

import { alumnoclaseGuard } from './alumnoclase.guard';

describe('alumnoclaseGuard', () => {
  const executeGuard: CanActivateFn = (...guardParameters) => 
      TestBed.runInInjectionContext(() => alumnoclaseGuard(...guardParameters));

  beforeEach(() => {
    TestBed.configureTestingModule({});
  });

  it('should be created', () => {
    expect(executeGuard).toBeTruthy();
  });
});
