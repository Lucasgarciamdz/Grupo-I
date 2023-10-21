import { TestBed } from '@angular/core/testing';
import { HttpClientTestingModule } from "@angular/common/http/testing";
import { PlanificacionService } from './planificacion.service';

describe('PlanificacionService', () => {
  let service: PlanificacionService;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [PlanificacionService]
    });
    service = TestBed.inject(PlanificacionService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
