/**
 * Negative Authorization Test Proposal
 * Note: This test is a proposal for the team's real pipeline. 
 * In the real codebase, `app` would be imported from the actual Medical Service.
 */

const request = require('supertest');
const express = require('express');

// 1. MOCK APP: Simulating the real Medical Service for the proposal
const app = express();
app.get('/api/v1/medical/123/vitals', (req, res) => {
    const token = req.headers.authorization;
    // If the token is a patient token, deny access (403)
    if (token === 'Bearer PATIENT_TOKEN_HERE') {
        return res.status(403).json({ error: 'Forbidden: Patients cannot access raw vitals' });
    }
    return res.status(200).json({ status: 'OK' });
});

// 2. THE TEST: Proving the negative scenario
describe('Negative Authorization Test', () => {
  it('should return 403 Forbidden when trying to access medical vitals without doctor role', async () => {
    const response = await request(app)
      .get('/api/v1/medical/123/vitals')
      .set('Authorization', 'Bearer PATIENT_TOKEN_HERE'); 
      
    expect(response.status).toBe(403);
  });
});